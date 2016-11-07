<template>
    <div id="modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">{{title}}</h4>
                </div>
                <div class="modal-body">
                    {{message}}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-dismiss="modal">{{button}}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
 var $ = require('jquery')

 export default {
     name: 'error',
     props: {
         title: {
             default () { return 'Error' }
         },
         message: '',
         button: {
             default () { return 'Close' }
         }
     },
     methods: {
         alert: function (msg) {
             this.message = msg
             $('#modal').modal({
                 backdrop: 'static'
             })
         }
     }
 }
</script>
