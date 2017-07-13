angular.module("myApp.user", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/user', {
            templateUrl: 'Webpages/user/user.html',
            controller: 'userController'
        });
    }])

    .controller("userController", function($scope, $http) {
        $http({
            method: 'GET',
            url: 'http://localhost:5000/user/' + $scope.userid,
            headers: {
                'Access-Control-Allow-Origin': 'http://localhost:8000'
            }
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
            console.log(response);
        }, function errorCallback(response) {
            console.log(response);
        })
    });