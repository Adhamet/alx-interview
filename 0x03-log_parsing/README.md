# alx-interview

Problem-Solving! YAY!

### Problem & Task: 
    Write a script that reads stdin line by line and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics
    1- Total file size: File size: <total size>
    2- Number of lines by status code:
        - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        - if a status code doesn’t appear or is not an integer, don’t print
        - format: <status code>: <number>
        - status codes should be printed in ascending order
