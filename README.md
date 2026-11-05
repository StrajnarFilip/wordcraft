# Screenshots for #3433 (a template opened from the file manager starts a new document)

The real app (`wordcraft`, debug build) in a private headless compositor (mutter, 1440×900), launched
with `Letterhead.dotx` on its command line, as a double-click in the file manager does; then a line
typed and Ctrl+S pressed through the control channel. The template is original (`make_template.py`).

- `3433-before-after.png`: the windows after Ctrl+S, cropped. Before: `storytold/wordcraft` main
  `db8d944c`. After: branch `fix/3433-shell-template-new-document` at `8abafa00`.
- `before-window.png`, `after-window.png`: the full windows.
- `after-protected-template.png`: after, a password-protected `Locked.dotx` on the command line,
  once its password was typed: a new Document1 with the template's text.
