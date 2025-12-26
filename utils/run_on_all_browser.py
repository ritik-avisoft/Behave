import subprocess # this will allow pytho to run external cmd
import sys

BROWSERS = ["chromium", "firefox", "webkit"]

def run_behave_tests():
    for browser in BROWSERS:
        print(f"--- Running Behave tests on {browser.capitalize()} browser ---")
        # Use subprocess to run the behave command with the -D (userdata) flag
        result = subprocess.run(
            [sys.executable, "-m", "behave", "-D", f"browser={browser}"],
            capture_output=True,
            text=True,
            check=False 
            # Set to True if you want the script to stop immediately on a failure 
            # and sys.executable make sure child use same version as parent
        )
        print(result.stdout)
        if result.stderr:
            print(f"Error for {browser}: {result.stderr}")
        
        if result.returncode != 0:
            print(f"Tests failed for {browser}")
            

if __name__ == "__main__":
    run_behave_tests()
    print("Test Executed on all three Browser....")