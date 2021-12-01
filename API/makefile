TAG="bluetel:latest"
.RECIPEPREFIX +=

.PHONY: clean image run all test

clean:
   @echo "Cleaning the building envrionment" \
   && rm -rf src/logs src/*.sqlite .image && docker rmi -f ${TAG}

.image:
   @echo "Building the docker image: ${TAG} ..." \
   && docker build -t ${TAG} . \
   && touch .image

image: .image 
   @echo "DONE"

test: image
   @echo "Executing the unit test" \
   && docker run --rm -it ${TAG} ./start test

run: image
   @echo "Running the container with latest image: ${APPNAME}:latest ..." \
   && docker run --rm -p 5000:5000 -it ${TAG} ./start run 

all: clean image test run
   @ echo "Runnnig"
