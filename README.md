# LibToHttp

A library to convert other libraries into simple servers, without having to manage raw API routes.
Great for OO fanatics.
  
    from libToHttp import router
  
    @router.route
    class MyLibrary:
      
      def my_function():
        return {'key': 'value'}
    
    router.run()

This automatically runs an HTTP server with the following route:

      /my_library/my_function/

which returns the JSON along with response headers and everything else needed to be an http response.

It adds all public methods (not beginning with underscore.)

The library can be rendered completely useless with almost zero overhead with

    router.config.API_ROUTES_ENABLED = False

Soon, there will be support for adding individual methods, setting a global url prefix to the router and method specific urls, specifying custom response functions that will be called before the http response is sent (right now it assumes json), and many more. 

This hasn't been used in the wild and is just a proof of concept, so use at your own risk.

#Installing

      git clone 
      virtualenv venv
      source venv/bin/activate
      pip install -r requirements.txt
    
#Testing
    
    make test
  runs the tests and shows coverage
      
    make autotest
  reruns the tests every time a file is saved (great with tmux etc.). 
    
    
