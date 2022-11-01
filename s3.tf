resource "aws_s3_bucket" "codepipeline_exam" {
  bucket = "pipeline-artifacts-exam"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.codepipeline_exam.id
  acl    = "private"
}