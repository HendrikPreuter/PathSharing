angular.module('myApp',
    ['ngRoute',
    'myApp.home',
    'myApp.groups',
    'myApp.about',
    'myApp.signup',
    'myApp.user',
    'myApp.invitations',
    'myApp.login'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});
    }])
    .controller('navController', ['$scope', '$http', function ($scope, $http) {
        $scope.username = localStorage.getItem('username');
        $scope.userid = localStorage.getItem('userid');
        console.log($scope.username);

        $scope.signout = function signout(){
            localStorage.clear();
            $http.defaults.headers.common.Token = null;
        };
    }]);