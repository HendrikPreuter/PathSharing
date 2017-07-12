angular.module("myApp.navigation", []).controller("navigationController", function($scope, $http) {
    $scope.username = localStorage.getItem('username');
    $scope.userid = localStorage.getItem('userid');

    $scope.signout = function signout(){
        localStorage.clear()
    };
});