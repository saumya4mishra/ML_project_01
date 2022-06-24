# ML_project_01
This is first ML project

creating CONDA environment

conda create -p venv python==3.7 -y

---to add file to git
git add filename
or
git add .

---to ignore file or folder from git

mention the file/ foldername in .gitignore file

-- to check git status
git status

-- to check all version mainained by git
git log

to create version/ commit all changes to git
git commit -m "message"

to send version/ changes to git
git push origin main

-- to check remote url
git remote -v

to setup CI/CD pipeline in heroku we need 3 information

1. HEROKU EMAIL_ID saumya4mishra@gmail.com
2. API KEY : d9d7b2c9-7673-4c8a-9523-81b2fe0a522b
3. APPLICATION: ml-regressor


BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .

e.g docker build -t ml-project:latest .

NOTE: image name for docker must be lowercase

--to list docker images
docker images

-- run docker image

docker run -p 5000:5000 -e PORT=5000 <docker_id>

-- to check running containers in docker
docker ps

--to stop docker container

docker stop <container_id>

