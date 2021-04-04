# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mainWindow.py'],
             pathex=['E:\\SPL3\\SPL3\\MainCode\\SpeechRecognition\\speech_recognition_tools',
             'C:\\Users\\S\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\PyQt5\\Qt5\\bin'],
             binaries=[],
             datas=[('images/inputIcon.png','images'),
                        ('nircmd.exe','.')],
             hiddenimports=["PyQt5.sip", 'PyQt5.QtGui', 'PyQt5.QtCore', 
                     'PyQt5.QtWidgets', 'numpy.core._dtype_ctypes', 'pyautogui'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='সহকারী-A Bangla Virtuall Assistant',
          debug=all,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)