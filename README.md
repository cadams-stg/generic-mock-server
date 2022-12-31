# Mock Third-party Integration Server

## Getting Started

- `make build` to build and initialize the container
- `make run` to start the server
- navigate to `http://localhost:8088/admin` to reach the admin site
   - django admin login: `admin / admin`
- paths are defined in `apps/example_response/urls.py`
- static templates are in `apps/example_response/templates/static_responses/`
- dynamic templates are in `apps/example_response/templates/dynamic_responses/`


### How to Create Static Responses
To define a simple, static response, create the template in the static response
directory, then define the path in URLs file. The template to be used and any
other arguments that should be passed to the template must be defined in the
path's `kwargs` argument.


### How to Create Dynamic Responses
To define a simple, dynamic response, create the template in the dynamic response
directory, then define the response in the Django admin site. Create a `CannedResponse`
object, which defines the path relative to `/example/dynamic/` and specifies a template.
Associated with the `CannedResponse`, `BodyMatch` objects can be defined to search the 
request body for regular expressions. If those regular expressions are matched, then
their named groups will be passed to the template associated to the `CannedResponse`.
Additionally, headers can be defined to be sent back with the response.