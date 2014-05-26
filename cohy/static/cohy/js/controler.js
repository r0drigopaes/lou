var cohyControllers = angular.module('cohyControllers', []);

cohyControllers.controller('StationListCtrl', ['$scope', '$http', '$location',
    function ($scope, $http, $location) {
        $scope.station_list = [];
        $http.get('/cohy/stations').success(function (data) {
            $scope.station_list = data

        });

        $scope.go = function (path) {
            $location.path(path);
        };
    }]);

cohyControllers.controller('StationNewCtrl', ['$scope', '$upload',
    function ($scope, $upload) {

        $scope.onFileSelect = function ($files) {
            var file = $files[0];
            $scope.upload = $upload.upload({
                url: 'station/new',
                // method: 'POST' or 'PUT',
                // headers: {'header-key': 'header-value'},
                // withCredentials: true,
                //data: {myObj: $scope.myModelObj},
                file: file  // or list of files: $files for html5 only
                /* set the file formData name ('Content-Desposition'). Default is 'file' */
                //fileFormDataName: myFile, //or a list of names for multiple files (html5).
                /* customize how data is added to formData. See #40#issuecomment-28612000 for sample code */
                //formDataAppender: function(formData, key, val){}
            }).progress(function (evt) {
                console.log('percent: ' + parseInt(100.0 * evt.loaded / evt.total));
            }).success(function (data, status, headers, config) {
                // file is uploaded successfully
                console.log(data);
            });
        };


    }]);

cohyControllers.controller('HomeCtrl', ['$translate', '$scope',
    function ($translate, $scope) {
        $scope.changeLanguage = function (lang_key) {
            $translate.use(lang_key);
        };
    }]);
