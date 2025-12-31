import uuid
<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
=======
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Integer, Float
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel, validator, UUID4
>>>>>>> a2600ba (update 30/12/2025- 4pm)
from typing import Optional

Base = declarative_base()

class DBAgent(Base):
    __tablename__ = "agents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
<<<<<<< HEAD
    role = Column(String, nullable=False)
=======
    description = Column(Text)
    module = Column(String, nullable=False)
    sub_module = Column(String)
    role = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    max_tokens = Column(Integer, nullable=False)
    system_prompt = Column(Text)
    status = Column(String, default="draft")  # draft, deployed, active, disabled
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DBRun(Base):
    __tablename__ = "agent_runs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id"))
    status = Column(String, default="started")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DBTask(Base):
    __tablename__ = "agent_tasks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id = Column(UUID(as_uuid=True), ForeignKey("agent_runs.id"))
    description = Column(Text, nullable=False)
    status = Column(String, default="queued")
<<<<<<< HEAD
    result = Column(Text, nullable=True) # Logging Result
=======
    result = Column(Text, nullable=True)  # Logging Result
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    error = Column(Text, nullable=True)  # Logging Error
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DBReflection(Base):
<<<<<<< HEAD
    __tablename__ = "agent_reflections" # Episodic Memory
=======
    __tablename__ = "agent_reflections"  # Episodic Memory
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id = Column(UUID(as_uuid=True), ForeignKey("agent_runs.id"))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DBFeedback(Base):
    __tablename__ = "agent_feedback"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id = Column(UUID(as_uuid=True), ForeignKey("agent_runs.id"))
<<<<<<< HEAD
    rating = Column(String, nullable=False)
=======
    rating = Column(Integer, nullable=False)
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# API Schemas
class AgentCreate(BaseModel):
    name: str
<<<<<<< HEAD
    role: str
=======
    description: Optional[str] = None
    module: str
    sub_module: Optional[str] = None
    role: str
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    system_prompt: Optional[str] = None

class AgentUpdate(BaseModel):
    status: str

    @validator('status')
    def status_must_be_valid(cls, v):
        allowed_statuses = ["draft", "deployed", "active", "disabled"]
        if v not in allowed_statuses:
            raise ValueError(f'Status must be one of {allowed_statuses}')
        return v
>>>>>>> a2600ba (update 30/12/2025- 4pm)

class TaskUpdate(BaseModel):
    status: str
    result: Optional[str] = None
    error: Optional[str] = None

class ReflectionCreate(BaseModel):
    content: str

# Response Models
class AgentResponse(BaseModel):
<<<<<<< HEAD
    id: uuid.UUID
    name: str
    role: str
    created_at: str

class RunResponse(BaseModel):
    id: uuid.UUID
    agent_id: uuid.UUID
=======
    agent_id: UUID4
    name: str
    description: Optional[str] = None
    module: str
    sub_module: Optional[str] = None
    status: str
    created_at: str
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    system_prompt: Optional[str] = None

class RunResponse(BaseModel):
    id: UUID4
    agent_id: UUID4
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    status: str
    created_at: str

class TaskResponse(BaseModel):
<<<<<<< HEAD
    id: uuid.UUID
    run_id: uuid.UUID
=======
    id: UUID4
    run_id: UUID4
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    description: str
    status: str
    result: Optional[str] = None
    error: Optional[str] = None
    created_at: str

class ReflectionResponse(BaseModel):
<<<<<<< HEAD
    id: uuid.UUID
    run_id: uuid.UUID
=======
    id: UUID4
    run_id: UUID4
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    content: str
    created_at: str

class RunTraceResponse(BaseModel):
    run: RunResponse
    tasks: list[TaskResponse]
    reflections: list[ReflectionResponse]

class FeedbackCreate(BaseModel):
    rating: int
    comment: Optional[str] = None

class FeedbackResponse(BaseModel):
<<<<<<< HEAD
    id: uuid.UUID
    run_id: uuid.UUID
=======
    id: UUID4
    run_id: UUID4
>>>>>>> a2600ba (update 30/12/2025- 4pm)
    rating: int
    comment: Optional[str] = None
    created_at: str

class RunStartResponse(BaseModel):
    run: RunResponse
    task: TaskResponse