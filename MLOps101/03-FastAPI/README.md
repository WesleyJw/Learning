## MLOps 101 Course

---

### Building an API with Python FastAPI

#### What is an API?

APIs (Application Programming Interface) are systems (software) that facilitate communication between two or more software applications. Therefore, an API serves as a connecting bridge between one system and another. In general, a backend software loads and transforms data, making it available for other systems. On the other end, a frontend application or any other application expects to receive the processed data. An API, through a set of definitions and protocols, enables these systems to share information. This means that the frontend software can make requests to obtain data, and vice versa, it can make requests to the backend to process certain activities.

![API](./img/api.png "A basic model of API")

A rest API comprises a client and a server. The server does not store states, meaning it has no memory. If the same request is made two or more times, the app consults the server to get the response. In general, an API is composed of a request and a response. Headers, HTTP methods and a body with requested parameters in a JSON format compost the request. The response is composed of a status code that defines if the request occurred without problems or if some issues were found. When the request is satisfied, the response contains a body with the data information requested. 

![Rest API](./img/rest_api.png "A basic model of Rest API")

#### Python FastAPI

FastAPI is a web framework for building APIs suing Python. The key features of this framework include (This key are presented in [FastAPI-Documentation](https://fastapi.tiangolo.com/)):

- Fast: Demonstrates very high performance, comparable to NodeJS and Go.

- Fast to code: Accelerates feature development speed.

- Fewer bugs: Results in a reduction of around 40% in human-induced errors, enhancing overall code reliability.

- Intuitive: Offers excellent editor support with comprehensive autocompletion, reducing time spent on debugging.

- Easy: Specifically designed to be user-friendly and easy to learn, minimizing the time developers spend reading documentation.

- Short: Aims to minimize code duplication, providing multiple features with each parameter declaration and ultimately reducing the occurrence of bugs.

- Robust: Generates production-ready code, accompanied by automatic interactive documentation for enhanced reliability.

- Standards-based: Aligns with and fully supports open standards for APIs, namely OpenAPI (formerly known as Swagger) and JSON Schema, ensuring compatibility and adherence to established norms.

#### Building an API

