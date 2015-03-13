import cx_Freeze

executables=[cx_Freeze.Executable("snakegame.py")]
cx_Freeze.setup(

                name="Snakey",
                options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakehead.png"]}},
                description="snakey game",
                executables=executables

                 






                
                )

