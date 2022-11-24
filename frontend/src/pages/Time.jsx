import React from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios'
const api = "http://127.0.0.1/timerapi/"

// function start() {
// 	const [time, setTime] = useState(null)

// 	useEffect(() => {
// 		axios.get("http://127.0.0.1:8000/timerapi/")
// 		.then((response) =>{
// 			setTime(response.data)
// 		})
// 		.catch(err => {
// 			console.table(err)
// 		})
// 	}, [])
// }


const Time = () => {
const [time, setTime] = useState(null)

	useEffect(() => {
		axios.get("http://127.0.0.1:8000/timerapi/")
		.then((response) =>{
			setTime(response.data)
		})
		.catch(err => {
			//console.table(err)
		})
	}, [])

//const nm = time.name	
//setInterval(start, 1000);
	return (
		<div>
			{time?.map((time, index) => 
				<div key={index}>
				{time.name} | {time.start_time} | {time.end_time}
				<br/>
				{typeof(time.start_time)}<br/>
				{typeof(new Date(time.start_time))}<br/>
				{typeof(new Date(time.end_time))}<br/>
				{new Date(time.end_time) - new Date(time.start_time)}<br/>
				{Math.floor(new Date(time.end_time) - new Date(time.start_time))/1000}<br/>
				{setInterval(
					Math.floor(new Date(time.end_time) - new Date(time.start_time))
					,1000)}
				{}
				</div>
			)}
			<h1>Hello</h1>
		</div>
	)
}

export default Time