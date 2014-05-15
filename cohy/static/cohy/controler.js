var cohyControllers = angular.module('cohyControllers',[]);

cohyControllers.controller('StationListCtrl',['$scope', '$http',
    function ($scope, $http) {
        $scope.station_list = [];
        $http.get('/cohy/stations').success(function (data) {
            $scope.station_list = data

        });
    }]);
