# environment
* ubuntu14.04
* docker0.11

# memo
* ubuntu13.10
* jenkins

# How to use
* start.shを起動
 * sshでコンテナ内部にログイン（root:root）
 * /data/jenkins_plugin.shを起動（プラグインが正しくインストールされない場合は少し時間をおいてから再度実行）
 * ブラウザからjenkinsのダッシュボードにアクセス
* 新規ジョブ作成
 * ジョブ名：任意のもの
 * フリースタイル・プロジェクトのビルドを選択
 * OKを押下
* プロジェクトを選択し、設定
 * ビルド
   * シェルの実行
     * シェルスクリプト（jenkinsシェルスクリプトを参照）
 * ビルド後の処理
   * Coberturaカバレッジ・レポートの集計
     * Cobertura XMLレポート パターン：coverage.xml
   * JUnitテスト結果の集計
     * テスト結果XML：pytest.xml
   * Publish HTML reports
     * HTML directory to archive：$WORKSPACE
     * Index page[s]：output.html
     * Report title：clonedigger Report
   * Report Violations
     * pylint
       * XML filename pattern：pylint.log
     * Source encoding：UTF-8
   * SLOCCountの分析結果の公開
     * SLOCCount レポート：sloccount.sc
   * 適用、保存を押下
* ホストの/root/workspace/aics/apiで作業後に、jenkinsのビルドを実行すれば、テストを行うことができる

# Jenkins
* Cobertura カバレッジ・レポートの集計
* JUnitテスト結果の集計
  * py.testによるテスト
* Publish HTML reports
  * clone diggerの出力HTMLを表示（重複コードの探索）
* Report Violations
  * pylintの出力（コード内の文法チェックや使用していないimportなどの指摘を行う）
* SLOCCountの分析結果の公開
  * 各コードの行数を出力
