# Dockerhubから、Python3.12のイメージをダウンロードしてコンテナにインストールする。バージョンを指定しないと自動的に最新版が設定される
FROM python:3.12

WORKDIR /working_dir
#説明：devcontainer.jsonで設定されたバインドマウント用ディレクトリ「workspace」をカレントディレクトリ（作業ディレクトリ）として設定しておく（後述のrequirements.txtを利用するため）

COPY . .
#説明：.devcontainer内部のファイルを全て、/working_dirにコピー


RUN pip install --upgrade pip
#説明： pipそのものを最新にしておく


RUN pip install -r requirements.txt
#説明：コンテナ内のカレントディレクトリにあるrequirements.txtを使って必要なモジュールなどを一括インストール


