# -*- mode: python -*-

block_cipher = None

bins = [
    ('*.dll', '.'),
]
files = [

('bgm', 'bgm'),
('sfx', 'sfx')
]
a = Analysis(['ritmsounds.py'],
             pathex=['.\\'],
             binaries=bins,
             datas=files,
             hiddenimports=["simplejson"],
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
          name='ritmsounds',
          debug=False,
          strip=False,
          upx=True,
          console=False )
