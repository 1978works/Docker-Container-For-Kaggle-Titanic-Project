# Dockerhubから、Python3.12のイメージをダウンロードしてコンテナにインストールする。バージョンを指定しないと自動的に最新版が設定される
FROM python:3.12
# コンテナ内部に設定した名前のディレクトリがなければ自動的に作成され、それが作業ディレクトリとして設定される
WORKDIR /vsc_workspace
# Titanic内のrequirements.txtを、コンテナ内部の作業ディレクトリ内（今回はvsc_workspace）にコピーする
# COPY ① ②（①：手元のPC内のファイルのパス、②：コンテナ内部のディレクトリのパス）
# ①について：Dockerfileは、Dockerfileのあるディレクトリがカレントディレクトリとして認識される
COPY requirements.txt /vsc_workspace
# pipそのものを最新にしておく
RUN pip install --upgrade pip
# コンテナ内の作業ディレクトリにあるrequirements.txtを使って必要なモジュールなどを一括インストール
RUN pip3 install -r requirements.txt


# .devcontainerディレクトリ内部のファイルを全て、WORKDIRとして設定した/vsc_workspaceへコピー
COPY . .


