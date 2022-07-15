#HACK BY XERRANOX
import sys, os, webbrowser

def _clear():
    os.system('cls')

def menu():
    _clear()

    print("""
\033[0;32m                                _   _  ____  _____ _   _  
\033[0;32m                               | | | |/    \|   __| |_/ |
\033[1;32m                               | |_| |  /\  |  |  |    /
\033[1;32m                               |  _  |  __  |  |__| |\ \ 
\033[0;32m                               |_| |_|_|  |_|_____|_| \_\ 

			           \033[1;36mMADE BY:\033[1;35m xerranox
  			           \033[1;36mVERSION:\033[1;35m   v0.3		      
		""")

    print("\033[1;36mSELECT YOUR OPTION TO USE:")
        
    print('''
\033[1;32m 1. IPLOGGER            \033[1;31m 7. Developing         \033[1;31m 13. Developing         \033[1;31m 19. Developing         \033[1;31m 25. Developing
\033[1;32m 2. IPGEOLOCALIZATION   \033[1;31m 8. Developing         \033[1;31m 14. Developing         \033[1;31m 20. Developing 	       \033[1;31m 26. Developing
\033[1;32m 3. NAMECHECK           \033[1;31m 9. Developing         \033[1;31m 15. Developing         \033[1;31m 21. Developing         \033[1;31m 27. Developing
\033[1;31m 4. Developing         \033[1;31m 10. Developing         \033[1;31m 16. Developing         \033[1;31m 22. Developing         \033[1;31m 28. Developing
\033[1;31m 5. Developing         \033[1;31m 11. Developing         \033[1;31m 17. Developing         \033[1;31m 23. Developing         \033[1;32m 29. ABOUT
\033[1;31m 6. Developing         \033[1;31m 12. Developing         \033[1;31m 18. Developing         \033[1;31m 24. Developing         \033[1;32m 30. EXIT
		''')

    selected = input("\033[1;35mSELECTED > ")

    if selected == "1":
        print("\033[1;32mSELECTED: 1")
        webbrowser.open_new_tab("https://grabify.link")
        menu()
    elif selected == "2":
        print("\033[1;32mSELECTED: 2")
        webbrowser.open_new_tab("https://ipgeolocation.io")
        menu()
    elif selected == "3":
        print("\033[1;32mSELECTED: 3")
        webbrowser.open_new_tab("https://namechk.com")
        menu()
    elif selected == "29":
        print("\033[1;32mSELECTED: 29")
        webbrowser.open_new_tab("https://xerranoxdev.web.app")
        menu()
    elif selected == "30":
        print("\033[1;32mSELECTED: 30")
        print("\033[1;37m")
        _clear()
        sys.exit()
    
menu()
