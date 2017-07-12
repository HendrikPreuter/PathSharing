angular.module("myApp.login", ['angular-jwt']).controller("loginController", ['$scope', '$http', '$location', 'jwtHelper', function ($scope, $http, $location, jwtHelper) {
    $scope.token = localStorage.getItem('token');
    if($scope.token !== null) {
        $http.defaults.header.common.Token = $scope.token;
        $location.path('../index.html');
    }

    $scope.login = function(user) {
        console.log('logging in.');
        var data = {
            'username': user.username,
            'password': user.password
        };
        console.log(data);
        $http.post("http://localhost:5000/login", data).then(function (response) {
            if(response.data.response === 'error') {
                console.log('Error')
            }

            else {
                $scope.token = response.data.token;
                $http.defaults.headers.common.Token = $scope.token;

                var userinfo = jwtHelper.decodeToken($scope.token);
                localStorage.setItem('username', userinfo.username);
                localStorage.setItem('userid', userinfo.id);
                window.location.href = '../../index.html';
            }
        })
    }
}]);