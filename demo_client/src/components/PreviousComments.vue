<template>
    <v-container>
        <v-subheader class="headline">Comment List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
        <v-col cols='4' v-show="$store.state.id === n.Writer" v-for="(n, i) in comment_list" 
          :key="i"
          >
          <Comment :comment_object="n" />
        </v-col>
        </v-row>
    </v-container>
</template>
<script>
import Comment from '@/components/Comment.vue';
export default {
    props: {

    },
    components: {Comment},
    data: () => ({
        
    }),
    asyncComputed: {
        comment_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/comment/`)
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
    },
    computed: {
  
    },
    methods: {
    }

}
</script>