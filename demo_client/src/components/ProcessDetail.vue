<template>
    <v-container>
        {{process_object}}
        <!-- <Process :process_object= "process_object" /> -->
        <v-timeline dense>
            <v-timeline-item
            v-for="n in items"
            :key="n"
            color="red lighten-2"
            large
            >
            <template v-slot:opposite>
                <span>Tus eu perfecto</span>
            </template>
            <v-card class="elevation-2">
                <v-card-title class="headline">{{n.title}}</v-card-title>
                <Comment v-for="m in comment_list" :key="m" :comment_object="m" v-show="m.Stage === n.stage"/>
                <v-card-text>
                    Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
                </v-card-text>
            </v-card>
            </v-timeline-item>
        </v-timeline>
    </v-container>
</template>
<script>
import Comment from '@/components/Comment'
export default {
    props: { },
    components: { Comment },
    data: () => ({
        items: [
            {   
            stage: 1,
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            stage: 2,
            color: '#8E8989',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
            {
            stage: 3,
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            stage: 4,
            color: '#8E8989',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
            {
            stage: 5,
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Review Complete',
            artist: 'Foster the People',
            },
        ],
    }),
    asyncComputed: {
        process_object: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/process/${this.process_id}`)
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        comment_list: {
            async get(){
                try {
                    let that = this
                    let commentArray = []
                    window.console.log(this.process_object.ProcessComments)
                    for (let n=0;n<this.process_object.ProcessComments.length;n++) {
                        const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/comment/${that.process_object.ProcessComments[n]}`)
                        commentArray.push(res.data)
                    }
                    window.console.log(commentArray)
                    return commentArray
                }catch(e) {
                    window.console.log(e)
                }
            }
        }
    },
    computed: {
        process_id: function() {
            let current_id = this.$router.currentRoute.path.split("/")[2]
            // window.console.log(current_id)
            return current_id
        }
    },
    methods: {
        
    }

}
</script>