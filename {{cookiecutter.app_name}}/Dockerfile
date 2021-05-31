# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}

FROM python:${INSTALL_PYTHON_VERSION} AS builder

WORKDIR /app

{%- if cookiecutter.use_pipenv == "True" %}
COPY ["Pipfile", "shell_scripts/auto_pipenv.sh", "./"]
RUN pip install --no-cache pipenv
RUN pipenv install
{%- else %}
COPY requirements requirements
RUN pip install --no-cache -r requirements/prod.txt
{%- endif %}

COPY autoapp.py ./
COPY {{cookiecutter.app_name}} {{cookiecutter.app_name}}
COPY .env.example .env

# ================================= PRODUCTION =================================
FROM python:${INSTALL_PYTHON_VERSION} as production

WORKDIR /app

RUN useradd -m sid
RUN chown -R sid:sid /app
USER sid
ENV PATH="/home/sid/.local/bin:${PATH}"

{%- if cookiecutter.use_pipenv == "True" %}
COPY ["Pipfile", "shell_scripts/auto_pipenv.sh", "./"]
RUN pip install --no-cache pipenv
RUN pipenv install
{%- else %}
COPY requirements requirements
RUN pip install --no-cache --user -r requirements/prod.txt
{%- endif %}

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisord_programs /etc/supervisor/conf.d

COPY . .

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "shell_scripts/supervisord_entrypoint.sh"]
CMD ["-c", "/etc/supervisor/supervisord.conf"]


# ================================= DEVELOPMENT ================================
FROM builder AS development

{%- if cookiecutter.use_pipenv == "True" %}
RUN pipenv install --dev
{%- else %}
RUN pip install --no-cache -r requirements/dev.txt
{%- endif %}
EXPOSE 2992
EXPOSE 5000
CMD [ {% if cookiecutter.use_pipenv == 'True' %}"pipenv", "run", {% endif %}"npm", "start" ]
