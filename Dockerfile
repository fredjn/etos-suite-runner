FROM python:3.9.0-buster AS build

COPY . /src
WORKDIR /src
RUN python3 setup.py bdist_wheel

FROM python:3.9.0-slim-buster

COPY --from=build /src/dist/*.whl /tmp
# hadolint ignore=DL3013
RUN pip install --no-cache-dir /tmp/*.whl && groupadd -r etos && useradd -r -m -s /bin/false -g etos etos && opentelemetry-bootstrap --action=install
ENV OTEL_EXPORTER_OTLP_ENDPOINT http://otl-collector.etos-dev.k8s.axis.com/v1/traces
ENV OTEL_TRACES_EXPORTER otlp_proto_http
ENV OTEL_RESOURCE_ATTRIBUTES service.name=ETOS Suite Runner,service.version=1.2.3,deployment.environment=development
ENV OTEL_PYTHON_EXCLUDED_URLS healthcheck,healthz,selftest/ping

USER etos

LABEL org.opencontainers.image.source=https://github.com/eiffel-community/etos-suite-runner
LABEL org.opencontainers.image.authors=etos-maintainers@googlegroups.com
LABEL org.opencontainers.image.licenses=Apache-2.0

CMD ["opentelemetry-instrument", "python", "-u", "-m", "etos_suite_runner"]
