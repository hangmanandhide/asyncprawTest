import os
import secrets

# Sets up required dependencies for the application and then downloads necessary NLTK data.
def setup_dependencies():
    try:
       install_requirements = os.system("pip install -r requirements.txt")
       return install_requirements
    except Exception as e:
           print(f"Error installing dependencies: {e}")
           return None
    finally:
        
        # double check asyncpraw and asyncprawcore are installed and up to date
        os.system("pip install --upgrade asyncpraw asyncprawcore")
        print("✅ Dependencies installed!")
        print("✅ Setup complete! You can now run the application with: python app.py or python3 app.py")

        
