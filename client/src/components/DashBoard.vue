<template>
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        justify="center"
      >
      <!-- <p>{{process_list}}</p> -->

      <Process v-for="(p, index) in process_list.results" :key="p._id"
      :pindex="index" :process="p"
      style="width: 85%"
      >
      </Process>
      </v-row>
    
    </v-container>    
</template>

<script>
  import Process from '@/components/Process'
  export default {
    components: {Process},
    data: () => ({
      drawer: null,
      e1: 1,
      detailShow: false,
      user: 2
    }),
    asyncComputed: {
      process_list: {
        async get() {
          try {
            const res = await this.$http.get(`http://localhost:8000/assistant/process`);
            return res.data
          }catch(e) {
            // console.log(e);
          }
        }
      }
    },
    created () {
      this.$vuetify.theme.dark = true
    },
  }
</script>