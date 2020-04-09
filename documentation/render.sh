echo "Usage: sh render.sh [publish]"
GUIDES=../neo4j-guides

function render {
$GUIDES/run.sh index.adoc index.html +1 "$@"
}

if [ "$1" == "publish" ]; then
        URL=guides.neo4j.com/sandbox/icij-panama-papers
        if hash aws 2>/dev/null; then
                aws s3 cp --acl public-read --recursive --exclude "*" --include "*.html" --include "*.png" --include "*.jpg" --include "*.gif" --include "*.csv" s3://${URL}/
                aws s3 cp --acl public-read index.html s3://${URL}
        else
                s3cmd put --recursive -P *.html img data s3://${URL}/
                s3cmd put -P index.html s3://${URL}
        fi
        echo "Publication Done"
elif [ "$1" == "render-only" ]; then
  URL=guides.neo4j.com/sandbox/icij-panama-papers
  render http://$URL
else
        URL=localhost:8001/sandbox/icij-panama-papers
        echo "Starting webserver at $URL Ctrl-C to stop"
        python $GUIDES/http-server.py
fi
