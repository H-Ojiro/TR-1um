# ----- ------ ----- ----- ------ ----- ----- ------ ----- 
# Copyright (c) 2026 jun1okamura <jun1okamura@gmail.com>  
# SPDX-License-Identifier: Apache-2.0
# ----- ------ ----- 
#
#  python3 MDP_TR-1um_to_IP62.py INPUT_TR-1um_GDS OUTPUT_IP62_GDS 
#
import sys
import subprocess
import click
import klayout

@click.command()
@click.argument(
    "rfile",    
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.argument(
    "input",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.argument(
    "output",
    type=click.Path(exists=False, file_okay=True, dir_okay=False),
)
@click.option("--top", required=True)

def MDP(rfile: str, input: str, output: str, top: str):
    klayout = "/usr/local/bin/klayout"
    #
    mdp_command = klayout + ' -b -r ' + rfile + ' -rd cellname=' + top + ' -rd input=' + input + ' -rd output=' + output
    mdp_process = subprocess.Popen(mdp_command.split())
    print(mdp_process.stdout)
    if mdp_process.returncode != 0:
        print(mdp_process.stderr)
        sys.exit(mdp_process.returncode)

if __name__ == "__main__":
    MDP()
