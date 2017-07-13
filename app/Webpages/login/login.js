angular.module("myApp.login", ['ngRoute', 'angular-jwt'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'Webpages/login/login.html',
            controller: 'loginController'
        });
    }])

    .controller("loginController", ['$scope', '$http', '$location', 'jwtHelper', function($scope, $http, $location, jwtHelper) {
        $scope.token = localStorage.getItem('token');
        if($scope.token !== null) {
            $http.defaults.header.common.Token = $scope.token;
            $location.path('/#!home');
        }

        $scope.login = function(user) {
            var data = {
                "username": user.username,
                "password": user.password
            };
            console.log(data);
            $http.post("http://localhost:5000/login", data).then(function (response) {
                if(response.data.response === 'error') {
                    console.log('Error');
                    $scope.error = "Something went wrong, try again";
                } else {
                    $scope.token = response.data.token;
                    $http.defaults.headers.common.Token = $scope.token;
                    localStorage.setItem('token', $scope.token);
                    window.location.href = '/#!home';
                }
            })
        }
    }]);