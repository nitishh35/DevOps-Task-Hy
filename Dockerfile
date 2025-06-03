# Builder stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --user -r requirements.txt

# Final stage using distroless
FROM gcr.io/distroless/python3
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .

ENV PYTHONPATH=/root/.local
ENV PATH=/root/.local/bin:$PATH

USER 1000:1000

EXPOSE 5000
CMD ["app.py"]

