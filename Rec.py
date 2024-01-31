import subprocess
import time
from pywinauto import Desktop, Application

app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)

control = app.window(title="Window Title").child_window(control_type="Button", title="Button Title")

# Perform an action on the control
control.click()