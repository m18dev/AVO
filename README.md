pythonbrew switch 2.7.2

依存ライブラリのインストール
pip install theano

pip install PyYAML
pip install Cython
pip install pillow

pilのinstall (pillowがあれば不要？)
ln -s /usr/local/include/freetype2 /usr/local/include/freetype
pip install PIL --allow-external PIL --allow-unverified PIL
参考
http://qiita.com/noblejasper/items/ee29e06ccb82ce97af5a

pylearn2のinstall

git clone git://github.com/lisa-lab/pylearn2.git
python setup.py develop
