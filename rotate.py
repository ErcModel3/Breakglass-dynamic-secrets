from rich.console import Console
from passlib.hash import sha512_crypt
import napalm

password_plain = "Password123"
password_encr = sha512_crypt.hash(password_plain)

rotation_template = f"""
system {{
    login {{
        user bg-srx1 {{
            uid 2003;
            class read-only;
            authentication {{
                encrypted-password "{password_encr}";
            }}
        }}
    }}
}}
"""

console = Console()

def rotate_breakglass_user():

    driver = napalm.get_network_driver("junos")
    device = driver(
        hostname = "10.0.0.50",
        username = "automation",
        password = "Password",
    )

    console.print("Deploying new password...", style="red")

    try:
        # Needs more logging somehow
        device.open()

        device.load_merge_candidate(config=rotation_template)

        device.commit_config()

    except Exception as e:
        console.print(f"[bold red]Deployment failed:[/bold red] {e}")
        try:
            device.discard_config()
        except:
            pass

    console.print("New password has been set...", style="green")
