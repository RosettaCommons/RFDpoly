# se3_transformer/utils/nvtx.py
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

@contextmanager
def nvtx_range(message: str) -> Iterator[None]:
    """
    Safe NVTX range context manager.

    - If running with CUDA + NVTX support, emits real NVTX ranges.
    - Otherwise, becomes a no-op (CPU-only CI, ROCm-only builds, etc).
    """
    try:
        import torch

        if torch.cuda.is_available() and hasattr(torch.cuda, "nvtx"):
            try:
                from torch.cuda.nvtx import range as _nvtx_range
                with _nvtx_range(message):
                    yield
                return
            except Exception:
                # CUDA available but NVTX missing/misconfigured -> fall back to no-op
                pass

        yield
    except Exception:
        # torch not importable or other unexpected env issue -> no-op
        yield

