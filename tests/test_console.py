import click.testing
import pytest

from etf_holdings_analysis import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_main_succeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
