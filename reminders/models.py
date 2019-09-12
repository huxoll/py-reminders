
type Reminder struct {
	ID        int64     `json:"id"`
	GUID      string    `sql:"size:48;unique_index:idx_guid;size=32" json:"guid"`
	Message   string    `json:"message"`
	CreatedAt time.Time `json:"createdAt"`
	UpdatedAt time.Time `json:"updatedAt"`
	DeletedAt time.Time `json:"-"`
}