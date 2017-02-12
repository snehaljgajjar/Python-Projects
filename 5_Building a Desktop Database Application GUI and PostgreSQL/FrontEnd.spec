# -*- mode: python -*-

block_cipher = None


a = Analysis(['FrontEnd.py'],
             pathex=['D:\\Python\\Projects\\5_Building a Desktop Database Application GUI and PostgreSQL'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='FrontEnd',
          debug=False,
          strip=False,
          upx=True,
          console=False )
