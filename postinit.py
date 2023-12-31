import gdb

post_commands = """
set follow-fork-mode parent
set attachp-resolution-method ask
"""

for command in post_commands.strip().splitlines():
  gdb.execute(command)
