FROM python:3.11-alpine
RUN apk add --no-cache curl
COPY app.py /app.py
EXPOSE 8080
CMD ["python","/app.py"]
