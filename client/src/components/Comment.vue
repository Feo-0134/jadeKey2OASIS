<template>
  <v-container>
    {{comment_list}}
    <v-card
      v-for="(p,index) in comment_list" 
      :key="p._id"
      :pindex="index"
      class="mx-auto"
      max-width="344"
      outlined
      >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">OVERLINE</div>
          <v-list-item-title class="headline mb-1">Headline 5</v-list-item-title>
          <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar
          tile
          size="80"
          color="grey"
        ></v-list-item-avatar>
      </v-list-item>

      <v-card-actions>
        <v-btn text>Button</v-btn>
        <v-btn text>Button</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
    data: ()=> ({
      stage_pk: this.$router.currentRoute.path.split('/')[1],
    }),
    asyncComputed: {
      comment_list: {
        async get() {
          try {
            const res = await this.$http.get(`http://127.0.0.1:8000/assistant/stage/${this.stage_pk}/comments_list/`);
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
