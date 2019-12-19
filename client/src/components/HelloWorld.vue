<template>
  <v-container>
    {{process_list}}
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',

  data: () => ({
  }),

  asyncComputed: {
    process_list: {
      async get() {
        try {
          const res = await this.$http.get(`http://127.0.0.1:8000/escdemo/`);
          return res.data
        }catch(e) {
          // console.log(e);
        }
      }
    }
  },
};
</script>
