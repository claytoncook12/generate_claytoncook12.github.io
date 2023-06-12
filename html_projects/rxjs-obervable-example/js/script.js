throw new Error(`Need to have a function that gets triggered on btn
click and then subscribe to ajax request inside of that
btn click function.`)

const dataHolder = document.getElementById("data");
const userID = document.getElementById("userId");
const btn = document.getElementById("loadUsers");

function addDataElement(text) {
  const dataDiv = document.createElement("div");
  dataDiv.innerText = text;
  dataHolder.appendChild(dataDiv);
}

const click = rxjs.fromEvent(btn, "click");

click
    .pipe(
        rxjs.switchMap(
            () => rxjs.ajax.ajax.getJSON(`https://reqres.in/api/users/${userID.value}`)
            .pipe(
                rxjs.operator.map(response => {
                    //addDataElement(`User Id: ${response.data.id} and email ${response.data.email}`)
                    console.log(response)
                    }
                )
            )
        )
    )
    .subscribe({
    next: (resp) => {console.log("To Next!")},
    error: (error) => console.log(error),
    complete: () => console.log("Complete!"),
    });
