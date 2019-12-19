<template>
  <v-container>
    {{comment_list}}

  </v-container>
</template>

<script>
export default {
    data: ()=> ({
    }),
    computed: {
      stage_pk() { 
        return this.$router.currentRoute.path.split('/')[1]
      }
    },
    asyncComputed: {
      comment_list: {
        async get() {
          try {
            const res = await this.$http.get(`http://localhost:8000/escdemo/stage/${this.stage_pk}`);
            return res.data
          }catch(e) {
            // console.log(e);
          }
        },
        default () {
            return [{fields:{title: 'undefined'}}] // for typeError: no default value
        }
      }
    },

}
</script>
