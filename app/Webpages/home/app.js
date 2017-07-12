angular.module("myApp", [])
    .controller("myController", ['$scope', '$http', function($scope, $http) {
        $scope.username = localStorage.getItem('username');
        $scope.userid = localStorage.getItem('userid');

        $scope.signout = function signout(){
            localStorage.clear();
            $http.defaults.headers.common.Token = null;
        };
    }]);