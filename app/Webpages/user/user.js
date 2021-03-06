angular.module("myApp.user", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/user', {
            templateUrl: 'Webpages/user/user.html',
            controller: 'userController'
        });
    }])

    .controller("userController", function($scope, $http) {
        if (!localStorage.getItem('token')) {
            window.location.href = '/#!login';
        }
        $http.get('http://localhost:5000/user').then(function (response) {
            if(response.data.response === "error"){
            } else {
                $scope.user_info = response.data;
            }
        });
    });