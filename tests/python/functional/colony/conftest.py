from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

import test_tools as tt
from hive_local_tools.constants import UNIVERSAL_BLOCK_LOGS_PATH


@pytest.fixture()
def alternate_chain_spec(block_log):
    return tt.AlternateChainSpecs.parse_file(
        UNIVERSAL_BLOCK_LOGS_PATH / "block_log_single_sign" / tt.AlternateChainSpecs.FILENAME
    )


@pytest.fixture()
def block_log():
    protected_block_log_destination = UNIVERSAL_BLOCK_LOGS_PATH / "block_log_single_sign"
    protected_block_log = tt.BlockLog(path=protected_block_log_destination / "block_log")
    return protected_block_log.copy_to(Path(tempfile.gettempdir()))
