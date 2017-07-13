angular.module("myApp.signup", ['ngRoute'])
    .config(['$routeProvider', function($routeProvider){
        $routeProvider.when('/signup', {
            templateUrl: 'Webpages/signup/signup.html',
            controller: 'signupController'
        });
    }])

    .controller("signupController", function($scope, $http){
        $scope.signup = function(user) {
            var data = {
                'username': user.username,
                'email': user.email,
                'password': user.password
            };
            $http.post("http://localhost:5000/user", data).then(function(response){
                if(response.data.response === "succes"){
                    alert("user created");
                    console.log("succes");
                    window.location.assign('/#!login');
                } else {
                    console.log(response.data.response);
                    alert(response.data.response);
                }
            })
        };
    });